# IT Services Task Bot

## Automation script to automatically assign Object IDs to calls in UniDesk:
UniDesk is a helpline software application that is commonly used throughout UK universities.
Any issues, queries or service requests related to any University department is logged through a call on this system. Hundreds of thousands of calls get processed in this way, and assigned
to the relevant uni team to solve. Each call/ticket has many attributes. One being the Object ID - the service the call is related to. Other attributes include a brief description, category, sub category and many more.

### Webscraping this application is highly tricky due to its complexity, and several layers of iframe embeddings. Simple, traditional webscraping navigation cannot be used. Executing code on the client side is required with nifty techniques to get passed the difficulties presented with this application.

# How this automation script works:
Javascript & Python:
1. Logs onto UniDesk
2. Navigates to the correct page containg the iframe of all the relevant calls.
3. An array of all these call's ticket numbers is created.
4. Each ticket in this array is searched, its attributes/ details and text information is gathered and returned by a JS promise on the server side.
5. An iteration loop is performed on the array to achieve this.
6. The tickets details are pushed into an object that is written to a file.
7. The JS script executes a python script
8. The python script reads the file containing the object of the ticket details.
9. Using python, the date is parsed based on specific categorisations, a huge tree of nested objects is created to represent the categories and subcategories of IT services at the University.
10. Methods such as array iteration and pattern mathcing based on keywords are used to sort through the data to conclude what object ID the ticket should be assigned.
11. A scoring system is used to increase the accuracy of the Object ID allocation. The more keywords relating to a specific service that are tagged on a ticket, the higher score the service will have for the ticket. The service with the highest score for that ticket, is likely to contain the Service's object ID relating to the ticket.
12. The Object ID is written back to a file to be retrived by th JS script.
13. The webscraping takes the value and enters it into the relevant section of the ticket on the UniDesk application.
