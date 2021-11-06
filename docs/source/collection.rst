Collection
===========

Let's walk through building a collection from a region in m/z and Retention Time 
and a list of Points.

.. code-block:: python

    from ms_collect.collection import Collection
    from ms_collect.scope import Scope
    from ms_collect.point import Point

    min_mz = 437.844
    max_mz = 438.94
    min_rt = 946.004
    max_rt = 981.107
    
    # A Scope represents a region in m/z and Retention Time
    scope = Scope([min_mz, max_mz, min_rt, max_rt])

    # A list of Point instances
    points = [ ... ]
    
    # Then build the collection instance
    my_collection = Collection(scope=scope, points=points)

    # Now we can perform various operations on our instance of the
    # collection class.

.. autofunction:: ms_collect.collection.Collection.__init__
.. autofunction:: ms_collect.collection.Collection.avg_mz