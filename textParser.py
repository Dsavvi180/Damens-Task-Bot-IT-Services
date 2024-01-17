from ServiceObjects import ServicesStr,SoftwareServices,UK_INT_Services,unidesk,N_A,no_subcategory,IdentityManagement,Telephones,BusinessReportingAnalytics,VSR,Infrastructure,CoreServicesAndSystems,EventsBooking,CollaborationTools,EmailAndDiary,PowerAppsAndAutomate,EventsAir,Zoom,MicrosoftDynamicsCRM,EventBooking,IDM,JIRA,ManagedMobileServices,Email,OneDrive,PowerBI,SharePoint,MicrosoftStream,Teams,SAPBusinessObjects,Serengeti,UniDesk,VisitorRegistrationSystem,WebHosting,WikiService,TestRail,ServiceAlerts,Miro
import re
import json

with open('details_object.json', 'r') as file:
    details_object = json.load(file)
if details_object['category'] is None or details_object['category'] == '' or details_object['subcategory'] is None or details_object['subcategory'] == '':
    print("Either category or subcategory is None or empty.")
    details_object=None
else:
    print("Both category and subcategory have values.")

with open('text.json', 'r') as data:
    text = json.load(data)

print(details_object)

Services = [
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


Categories = {
    CoreServicesAndSystems: { EventsBooking: { "EventsAir": EventsAir,
                                               "Event Booking": EventBooking},
                               
                               CollaborationTools: { "Zoom": Zoom,
                                                     "Microsoft Dynamics CRM": MicrosoftDynamicsCRM,
                                                     "JIRA": JIRA,
                                                     "OneDrive": OneDrive,
                                                     "SharePoint": SharePoint,
                                                     "MicrosoftStream": MicrosoftStream,
                                                     "Teams": Teams,
                                                     "Test Rail": TestRail,
                                                     "Service Alerts": ServiceAlerts,
                                                     "Miro": Miro,
                                                     "Web Hosting": WebHosting},
                                EmailAndDiary : { "Email": Email} ,
                                BusinessReportingAnalytics : {  "Power BI": PowerBI,
                                                                "SAP Business Objects": SAPBusinessObjects},
                               VSR: {"Visitor Registration System": VisitorRegistrationSystem}
                               },

    Infrastructure:          { SoftwareServices:{"Power Apps and Power Automate": PowerAppsAndAutomate},
                               IdentityManagement:{"IDM (Identity Management)": IDM},
                               Telephones: {"Managed Mobile Service": ManagedMobileServices}
                               },
    UK_INT_Services:         { unidesk: { "UniDesk": UniDesk}},
    N_A:                     { no_subcategory: {"Serengeti": Serengeti,
                                                "Wiki Service": WikiService}
                               }
} 


def keywordScore(text1, flagged_services):
    flagged_services_scores = []
    for i in flagged_services:
       score = 0
       
       for keyword in ServicesObj[ServicesStr.index(i)].keywords:
           if keyword.lower() in text1.lower():
               score +=1
       flagged_services_scores.append(score)
    #    print("flagged services scores",len(flagged_services_scores), flagged_services_scores)
    largest_score = max(flagged_services_scores)
    if len([index for index,value in enumerate(flagged_services_scores)if value == largest_score]) ==1 :
        most_relevant_service = ServicesObj[ServicesStr.index(flagged_services[flagged_services_scores.index(largest_score)])]
        ObjectIDFinal = most_relevant_service.objectID
        print(ObjectIDFinal)
        return ObjectIDFinal
    else: 
        print("After performing keyword search, several services have the same score:")
        final_services = []
        for p in [index for index, value in enumerate(flagged_services_scores) if value == largest_score]:
          final_services.append(flagged_services[p])
        print(final_services)
        ObjectIDFinal = N_A + " More than one service has the same score"
        return ObjectIDFinal
    
def patternMatchParser(text, ListOfServices):
    print("Parsing with pattern match and maybe regex")
    #This function has two roles:
    #1. Find the service involved from scratch without knowledge of details_object, incase this section has not been filled in
    #2. Find the service involved from a narrowed down selection of possible services based on the calls category and subcategory
    if details_object is None:
            details_object['Brief Description'] = None
            ListOfServices = ServicesStr
    else:
            ListOfServices = ListOfServices
    print("XYZ", ListOfServices)
    if 'subject' in text.lower().split():
       edited_text = " ".join(text.split()[(text.lower().split().index('Subject:')):]).lower()
    elif 'hi' in text.lower().split():
          edited_text = " ".join(text.split()[text.lower().split().index('hi'):]).lower()
    else:
          edited_text = text.lower()
    flagged_services = []
    print(edited_text)
    
    for z in ListOfServices:
        if z.lower() in edited_text.lower() or z.lower() in details_object['Brief Description']:
            print(z)
            flagged_services.append(z)  
#     print("Flagged Services",flagged_services)
    if len(flagged_services) == 1:
        #     print("Only one flagged service")
            ObjectIDFinal = ServicesObj[ServicesStr.index(flagged_services[0])].objectID
            print(ObjectIDFinal)
            print("executed C")
            return ObjectIDFinal
    elif len(flagged_services) == 0:
            print("no flagged service, keyword search anyway:")
            ObjectIDFinal = keywordScore(edited_text, ServicesStr)
            print("executed d",ObjectIDFinal)
            return ObjectIDFinal
    else:
            #narrow down 
            print("Sevral flagged services. Keyword search required.")
            ObjectIDFinal = keywordScore(edited_text, flagged_services)
            return ObjectIDFinal
    

#Placing calls into CATEGORIES:
print(details_object)
categoriesList = [CoreServicesAndSystems, Infrastructure, UK_INT_Services, N_A]
subcategoryList = None
categoryNode = details_object['category'] if details_object else None
subcategoryNode = details_object['subcategory'] if details_object else None
print("Subcategory NODE",subcategoryNode)
#servicesList = None
subcategories_with_one_service = [SoftwareServices, IdentityManagement, Telephones, unidesk, VSR, EmailAndDiary]

def GenerateObjectID(text):
  
  if details_object is not None:
      for i in categoriesList:
        if categoryNode == i:
          print("Category:",categoryNode)
          subcategoryList = list(Categories[i].keys())
          print(f"List of subcategories in {categoryNode}:",subcategoryList)
          for x in subcategoryList:
            if subcategoryNode == x:
              servicesList = list(Categories[i][x].keys())
              print("Subcategory:",x ,f"\nList of services in {x}", servicesList)
              if x in subcategories_with_one_service:
                ObjectIDFinal = Categories[i][x][list(Categories[i][x].keys())[0]].objectID
                print(ObjectIDFinal)
                print("Executed A")
                return ObjectIDFinal
              else:
                #potential services defined in servicesList 
                #briefDescription = details_object['Brief Description']
                ObjectIDFinal = patternMatchParser(text, servicesList)
                print("Executed B")
                return ObjectIDFinal
  else:
    ObjectIDFinal = patternMatchParser(text, ServicesStr)
    return ObjectIDFinal
   

ObjectIDFinal = GenerateObjectID(text)

print("The final Object ID answer is:", ObjectIDFinal)

if 'N/A' in ObjectIDFinal:
  ObjectIDFinal = 'N/A'
print(ObjectIDFinal)
with open('ObjectIDFinal.txt', 'w') as file2:
    file2.write(ObjectIDFinal)