const {expect} = require('@jest/globals');
import  { grabEl, grabEls, listen } from '.\helpers.js';

// function getElementsById(ids) {
//     var idList = ids.split(" ");
//     var results = [], item;
//     for (var i = 0; i < idList.length; i++) {
//         item = document.getElementById(idList[i]);
//         if (item) {
//             results.push(item);
//         }
//     }
//     return(results);
// }
// doStuff(getElementsById("myCircle1 myCircle2 myCircle3 myCircle4"));


describe('Test the uppload of hello-world application on the cameras', () => {

    test('Search in the interface if there is hello-world application', () =>{
        let content = grabEl.getElementsByClassName("Apps__AppsContent-sc-3791tt-0.edSaLB");
        expect(content).toContain('hello_world')
    })
})