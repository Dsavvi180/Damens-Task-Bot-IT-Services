// import { PuppeteerExtra } from "puppeteer-extra";
// import { PuppeteerExtraPlugin } from "puppeteer-extra";
// To use ES6 syntax for imports as above, add: "type":"module" to package.json

const puppeteer = require("puppeteer-extra");
const StealthPlugin = require("puppeteer-extra-plugin-stealth");
const fs = require("fs");
const { execSync } = require("child_process");

puppeteer.use(StealthPlugin());

function delay(time) {
  return new Promise(function (resolve) {
    setTimeout(resolve, time);
  });
}

puppeteer
  .launch({ headless: false })
  .then(async (browser) => {
    console.log("Running tests..");
    //Opening browser to UniDesk URL, logging in and navigating to the homepage
    //Potential workaround: pass log in credentials to browser in form of browser.cookies to bypass active log in
    const page = await browser.newPage();
    await page.goto("https://ed.unidesk.ac.uk/");

    await page.waitForSelector("#secure");
    await page.click("#secure");

    await page.waitForSelector("#login");
    await page.type("#login", "dsavvas");

    await page.waitForSelector("#submit");
    await page.click("#submit");

    await page.waitForSelector("#password");
    await page.type("#password", "*****", { delay: 100 });

    await page.waitForSelector("#submit");
    await page.click("#submit");
    await delay(5000);

    //Selecting No Object ID widget embedded in an iframe
    //Note - the page object in puppeteer does not have a querySelectorAll() method.
    //Overcome this by executing the code in the console(client side) using page.evaluate()

    let call_text;

    await page
      .evaluate(() => {
        async function webber() {
          const iframeNodeList = document.querySelectorAll("iframe");
          iframeNodeList;
          const iframeDocument = iframeNodeList.item(0).contentDocument;
          const iframeElement = iframeDocument.querySelector(
            '[guielement="selections_reports_item"]'
          );
          await iframeElement.click();

          function delay(time) {
            return new Promise(function (resolve) {
              setTimeout(resolve, time);
            });
          }
          await delay(4000);
          //naviagtion from inside No Object ID page

          const contentDocFrame = Array.from(
            document.querySelectorAll("iframe")
          )[1].contentDocument;

          await delay(1000);

          contentDocFrame
            ? console.log(`contentDocFrame present`)
            : console.log(`contentDocFrame not present`);

          const targetFrame = contentDocFrame.querySelectorAll("iframe")[0];
          await delay(1000);

          targetFrame
            ? console.log(`targetFrame present`)
            : console.log(`targetFrame not present`);

          calls = targetFrame.contentDocument.documentElement;
          await delay(1000);

          calls
            ? console.log(`calls present`)
            : console.log(`calls not present`);

          calls2 = calls.querySelector('form[name="main"]');
          await delay(1000);

          calls2
            ? console.log(`calls2 present`)
            : console.log(`calls2 not present`);

          calls3 = calls2.querySelector(
            'iframe[id="outergridframe"]'
          ).contentDocument;
          await delay(1000);

          calls3
            ? console.log(`calls3 present`)
            : console.log(`calls3 not present`);

          calls4 = calls3.querySelector(
            'iframe[id="gridframe"]'
          ).contentDocument;
          await delay(1000);

          calls4
            ? console.log(`calls4 present`)
            : console.log(`calls4 not present`);

          calls5 = calls4.querySelector('iframe[id="columns"]').contentDocument
            .body;
          await delay(1000);

          calls5
            ? console.log(`calls5 present`)
            : console.log(`calls5 not present`);

          calls6 = calls5.querySelector("#columnsscroll");
          await delay(1000);

          calls6
            ? console.log(`calls6 present`)
            : console.log(`calls6 not present`);
          //Use the ID to loop over every call in callNumbersArray
          calls7 = calls6.querySelector("#row_12_cell_3");
          callNumbers = calls6.querySelector("#_naam");
          callNumbersElementArray = Array.from(
            callNumbers.querySelectorAll("span")
          );
          callNumbersArray = [];
          for (i = 0; i < callNumbersElementArray.length; i++) {
            callNumbersArray.push(callNumbersElementArray[i].textContent);
          }
          console.log(callNumbersArray);
          // START HERE
          //
          //
          //
          //
          //ATTENTION
          //
          //
          //
          //
          //
          //
          //ATTENTION
          ///////
          /////////
          //Call this function to search for each ticket and access the info in the ticket. Map over each call number executing this function each time.
          //implement the following for calls that are partial, and skip that index in the loop
          // if (callNumbersArray[call_index].includes("\\")) {
          call_index = 3;
          async function searchCallNumberFromArray() {
            searchButton = Array.from(
              document.querySelectorAll('[guielement="icon-button"]')
            )[1];
            searchButton.click();
            await delay(500);
            const inputElement = document.querySelector(
              '[placeholder="Search…"]'
            );
            //DONT FORGET TO COMMENT THIS OUT AND COMMENT IN THE DYNAMIC CODE
            // inputElement.value = callNumbersArray[call_index];
            inputElement.value = "I221028-1408";
            inputElement.dispatchEvent(new Event("input", { bubbles: true }));

            searchIcon = document.querySelector(
              '[guielement="quicklaunch_search_button"]'
            );
            searchIcon.click();
            await delay(10000);
            c1 = document.querySelectorAll("iframe")[2].contentDocument;

            await delay(1000);
            text1 = c1.querySelector('[guielement="crt-content-label"]');
            text = text1.textContent;

            const contentDocFrame2 = Array.from(
              document.querySelectorAll("iframe")
            )[2].contentDocument;
            await delay(1000);

            if (callNumbersArray[call_index].includes("\\")) {
            } else {
              detailsWidget = Array.from(
                contentDocFrame2.querySelectorAll(
                  '[guielement="mg-minimized-content"]'
                )
              )[1];
            }
            await delay(1000);
            detailsWidget.click();
            console.log("clicked");
            await delay(2000);
            const contentDocFrame3 = Array.from(
              document.querySelectorAll("iframe")
            )[2].contentDocument;
            await delay(1000);
            detailsText = Array.from(
              contentDocFrame3.querySelectorAll(
                '[guielement="mg-expanded-content"]'
              )
            )[0];
            const detailsArray = Array.from(
              detailsText.querySelectorAll("input")
            ).slice(0, 5);

            const detailsObject = {
              "Brief Description": detailsArray[0].value,
              Entry: detailsArray[1].value,
              "Call Type": detailsArray[2].value,
              category: detailsArray[3].value,
              subcategory: detailsArray[4].value,
            };

            console.log(detailsObject);

            //navigation in actual call
            return { text, detailsObject };
          }

          return searchCallNumberFromArray();
        }
        return webber();
      })
      .then((result) => {
        console.log(result);
        hasClientScriptFinished = result.hasClientScriptFinished;
        call_text = result.text;
        details_object = result.detailsObject;

        fs.writeFileSync("details_object.json", JSON.stringify(details_object));
        fs.writeFileSync("text.json", JSON.stringify(call_text));
        // use the below code to automatically trigger the python3 script
        execSync(
          "python3 /Users/damensavvasavvi/Desktop/Coding-Projects/Task-Bot/textParser.py"
        );
      });
    const finalObjectID = fs.readFileSync("ObjectIDFinal.txt", "utf-8");
    console.log(finalObjectID);
    await delay(1000);
    await page.evaluate((finalObjectID) => {
      async function settingObjectID(finalObjectID) {
        // const contentDocFrame3 = Array.from(
        //   document.querySelectorAll("iframe")
        // )[2].contentDocument;
        // ObjectIDText = Array.from(
        //   contentDocFrame3.querySelectorAll(
        //     '[guielement="mg-expanded-content"]'
        //   )
        // )[1];
        // objectArray = Array.from(ObjectIDText.querySelectorAll("input"));
        console.log("Final ObjectID input:" + finalObjectID);
        // console.log(ObjectIDText, objectArray);
      }
      settingObjectID(finalObjectID);
    }, finalObjectID);
    // await browser.close();

    console.log(
      `Call text: ${call_text}\n Details text: ${
        (details_object["category"],
        details_object["Brief Description"],
        details_object["subcategory"])
      }`
    );
  })
  .catch((error) => console.error(error));

//CODE FOR SETTING OBJECT ID:
// Get the element by its ID
// var inputElement = document.getElementById('c2P1R_H8');

// // Check if the element exists
// if (inputElement) {
//     // Set the value attribute
//     inputElement.value = 'YourNewValue';

//     // Log or perform any other actions as needed
//     console.log('Value attribute set to: ' + inputElement.value);
// } else {
//     console.error('Element with ID c2P1R_H8 not found');
// }
