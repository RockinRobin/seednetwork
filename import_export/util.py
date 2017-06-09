from django.db.models.fields.related import RelatedField
from django.db.models.fields import Field
import csv

def export(querylist, filename):
    """
    Given a querylist, exports the entries to a .csv file

    Parameters
    -----------
    querylist: django.db.models.query.QuerySet
        List of database entries to export. Usually generated
        from a database query. 
    filename: str
        Path to filename for the export

    Examples
    ---------
    >>> from django.contrib.auth.models import User
    >>> querylist = User.objects.all()  # finds all users
    >>> export(querylist, '/tmp/users.csv')
    """
    entry = querylist[0]
    header = [h for h in entry._meta.get_fields() \
        if isinstance(h, Field)]
    header_names = [h.name for h in header]
    with open(filename, 'w') as fid:
        writer = csv.DictWriter(fid, header_names)
        writer.writeheader()
        for query in querylist:
            row = {h.name: str(getattr(query, h.name, '')) \
                      for h in header}
            for h in header:
                if isinstance(h, RelatedField):
                    try:
                        row[h.name] = str(getattr(query, h.name).pk)
                    except Exception, e:
                        print 'Failed to set pk for ', h.name
                        print e
            writer.writerow(row)


def import_entries(model, filename, save=False):        
    """
    Given a model, adds new entries populated from .csv file

    Parameters
    -----------
    model: django.db.models.Model
        A user-defined model class that has a django model parent
    filename: str
        Path to filename from which new data will be populated
    save: bool, optional
        Default is False. If True, will call entry.save() to actually
        put this entry into the database. 

    Returns
    --------
    entries : List(model)
        A list of new models for each entry in the .csv file

    Notes
    ------
    This function works with the export function in this module. 
    That is, it expect a header with field names to be present

    The save flag is present in case there are any Foreign keys
    that the user needs to take care of manually. 

    Example
    --------
    >>> from django.contrib.auth.models import User
    >>> users = import_entries(User, '/tmp/users.csv', False)
    >>> # Do any check and fix any broken relationship
    >>> for user in users: user.save()
    """
    with open(filename, 'r') as fid: 
        reader = csv.DictReader(fid) 
        header = reader.fieldnames
        raw_entries = [r for r in reader]

    entries = []
    for raw in raw_entries:
        entry = model()
        for key, val in raw.iteritems():
            try:
                field = entry._meta.get_field(key) 
                if isinstance(field, RelatedField):
                    setattr(entry, key, \
                        field.remote_field.model.objects.get(pk=val))
                else:
                    setattr(entry, key,
                        field.to_python(val))
            except Exception, e:
                print key, ":", val, ">>>", e
        if save:
            entry.save()
        entries.append(entry)
    return entries
   
