from typing import List

class ObjectDetails:
    def __init__(self, category: str, subcategory: str, objectID: str, keywords: List[str]):
        self.category = category
        self.subcategory = subcategory
        self.objectID = objectID
        self.keywords = keywords
#Global Variables
#Categories
CoreServicesAndSystems = "Core Services and Systems"
#subcategories
EventsBooking = "Event Booking"
CollaborationTools = "Collaboration Tools"
EmailAndDiary = "Email and Diary"
BusinessReportingAnalytics = "Business Reporting & Analytics"
VSR = "Visitor Registration"

Infrastructure = "Infrastructure"
#subcategories
SoftwareServices = "Software Services"
IdentityManagement = "Identity Management (IDM)" #'See linked object' in wiki
Telephones = "Telephones"

UK_INT_Services = "UK and International Services"
#subcategories
unidesk = "UniDesk"
N_A = "N/A"
#subcategories
no_subcategory = ""

PowerAppsAndAutomate = ObjectDetails( category = Infrastructure,
                                      subcategory = SoftwareServices, 
                                      keywords=[],
                                      objectID= "N/A" )
EventsAir = ObjectDetails( category = CoreServicesAndSystems,
                           subcategory = EventsBooking, 
                           keywords=[],
                           objectID= "EventsAir")
Zoom = ObjectDetails( category = CoreServicesAndSystems,
                      subcategory = CollaborationTools, 
                      keywords=[],
                      objectID= "Zoom")
MicrosoftDynamicsCRM = ObjectDetails(category = CoreServicesAndSystems, 
                                     subcategory=CollaborationTools, 
                                     keywords=[],
                                     objectID="Enquiry Management CRM")
EventBooking = ObjectDetails(category = CoreServicesAndSystems, 
                             subcategory=EventsBooking, 
                             keywords=[],
                             objectID="Event Booking")
IDM = ObjectDetails(category=Infrastructure,
                    subcategory=IdentityManagement, 
                    keywords=[],
                    objectID="Identity Mangement (IDM)")
JIRA = ObjectDetails(category = CoreServicesAndSystems, 
                     subcategory=CollaborationTools, 
                     keywords=["JIRA"],
                     objectID="JIRA")
ManagedMobileServices  = ObjectDetails(category=Infrastructure, 
                                       subcategory=Telephones, 
                                       keywords=[],
                                       objectID="Managed Mobile Services")
Email = ObjectDetails(category = CoreServicesAndSystems, 
                      subcategory= EmailAndDiary, 
                      keywords=["Office 365", "email"],
                      objectID="Email and Diary")
OneDrive = ObjectDetails(category = CoreServicesAndSystems, 
                         subcategory=CollaborationTools, 
                         keywords=["Office 365"],
                         objectID="Office365")
PowerBI = ObjectDetails(category=CoreServicesAndSystems,
                        subcategory=BusinessReportingAnalytics,
                        keywords=["Office 365"],
                        objectID="Power BI")
SharePoint = ObjectDetails(category= CoreServicesAndSystems,
                           subcategory=CollaborationTools,
                           keywords=["Sharepoint", "sharepoint", "Office 365"],
                           objectID="SharePoint")
MicrosoftStream = ObjectDetails(category=CoreServicesAndSystems,
                                subcategory=CollaborationTools,
                                keywords =["Office 365"],
                                objectID="Office 365")
Teams = ObjectDetails(category=CoreServicesAndSystems,
                      subcategory=CollaborationTools,
                      keywords=["Teams", "Microsoft Teams", "Office 365"],
                      objectID="Teams on Office365")
SAPBusinessObjects = ObjectDetails(category=CoreServicesAndSystems,
                                   subcategory=BusinessReportingAnalytics,
                                   keywords=[],
                                   objectID="Business Objects BI Launchpad, Business Objects Explorer ,Business Reporting and Analytics")
Serengeti = ObjectDetails(category="", subcategory="", keywords=[], objectID="Serengeti")
UniDesk = ObjectDetails(category=UK_INT_Services,
                        subcategory=unidesk,
                        keywords = [],
                        objectID="UniDesk Institution")
VisitorRegistrationSystem = ObjectDetails(category=CoreServicesAndSystems,
                                          subcategory=VSR,
                                          keywords=[],
                                          objectID="Visitor Registration")
WebHosting = ObjectDetails(category=CoreServicesAndSystems,
                           subcategory=CollaborationTools,
                           keywords=[],
                           objectID="Web and Application Hosting")
WikiService = ObjectDetails(category= N_A,
                            subcategory=no_subcategory,
                            keywords=[],
                            objectID="Identity Mangement (IDM)")
TestRail = ObjectDetails(category=CoreServicesAndSystems,
                         subcategory=CollaborationTools,
                         keywords=[],
                         objectID="User Testing")
ServiceAlerts = ObjectDetails(category=CoreServicesAndSystems,
                              subcategory=CollaborationTools,
                              keywords=[],
                              objectID="Service Alerts")
Miro = ObjectDetails(category=CoreServicesAndSystems,
                     subcategory=CollaborationTools,
                     keywords=[],
                     objectID="TBA")

ServicesStr = [
    "PowerAppsAndAutomate",
    "EventsAir",
    "Zoom",
    "MicrosoftDynamicsCRM",
    "EventBooking",
    "IDM",
    "JIRA",
    "ManagedMobileServices",
    "Email",
    "OneDrive",
    "PowerBI",
    "SharePoint",
    "MicrosoftStream",
    "Teams",
    "SAPBusinessObjects",
    "Serengeti",
    "UniDesk",
    "VisitorRegistrationSystem",
    "WebHosting",
    "WikiService",
    "TestRail",
    "ServiceAlerts",
    "Miro"
]

ServicesObj = [
    PowerAppsAndAutomate,
    EventsAir,
    Zoom,
    MicrosoftDynamicsCRM,
    EventBooking,
    IDM,
    JIRA,
    ManagedMobileServices,
    Email,
    OneDrive,
    PowerBI,
    SharePoint,
    MicrosoftStream,
    Teams,
    SAPBusinessObjects,
    Serengeti,
    UniDesk,
    VisitorRegistrationSystem,
    WebHosting,
    WikiService,
    TestRail,
    ServiceAlerts,
    Miro
]