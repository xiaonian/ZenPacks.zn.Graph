from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
class ExtendGraph(Device):

    _properties = Device._properties
    factory_type_information = (
    {
        'id'             : 'Device',
        'meta_type'      : 'Device',
        'description'    : """Base class for all devices""",
        'icon'           : 'Device_icon.gif',
        'product'        : 'ZenModel',
        'factory'        : 'manage_addDevice',
        'immediate_view' : 'devicedetail',
        'actions'        :
        (
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'deviceStatus'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'osdetail'
            , 'name'          : 'OS'
            , 'action'        : 'deviceOsDetail'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'swdetail'
            , 'name'          : 'Software'
            , 'action'        : 'deviceSoftwareDetail'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'events'
            , 'name'          : 'Events'
            , 'action'        : 'viewEvents'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'perfServer'
            , 'name'          : 'Graphs'
            , 'action'        : 'viewDevicePerformance'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'perfServer'
            , 'name'          : 'Portal'
            , 'action'        : 'viewDevicePerformance'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'edit'
            , 'name'          : 'Edit'
            , 'action'        : 'editDevice'
            , 'permissions'   : ("Change Device",)
            },
        )
     },
    )

