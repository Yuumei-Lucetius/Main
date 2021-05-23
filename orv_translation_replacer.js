/* 
    -- Updated up to ch.365 --

    Description:
    This code was prepared to substitute new translations (ch.363 onward) of the "Omniscient Reader's Viewpoint" web novel on novelchapter.com with older variants, for readers who preferred them.

    How to run this code:
    1. Open the Dev console in your browser (i.e. Google Chrome - F12)
    2. Paste the code on this page into the console and run it (i.e. hit Enter)

    Alternative save and run it as a snippet:
    https://developer.chrome.com/docs/devtools/javascript/snippets/
    
    Source: 
    https://stackoverflow.com/a/34559316/2341469
*/

function walkText(node) {
    if (node.nodeType == 3) {
        /* 
            Replace additional text by appending the following line below:
            node.data = node.data.replace(/oldtext/gi, "newtext");
        */
        
        /* System */
        node.data = node.data.replace(/Fable/g, "Story");
        node.data = node.data.replace(/Storys/g, "Stories");
        node.data = node.data.replace(/Historical Figure-grade/g, "Great-grade");
        node.data = node.data.replace(/Story-grade/g, "Narrative-grade");
        node.data = node.data.replace(/Transcender/gi, "Transcendent");

        /* Main characters */
        node.data = node.data.replace(/Kim Dok-Ja/gi, "Kim Dokja");
        node.data = node.data.replace(/Dok-Ja/gi, "Dokja");
        node.data = node.data.replace(/Yu Ho-Seong/gi, "Yu Hosung");
        node.data = node.data.replace(/Ho-Seong/gi, "Hosung");
        node.data = node.data.replace(/Yu Sang-Ah/gi, "Yoo Sangah");
        node.data = node.data.replace(/Sang-Ah/gi, "Sangah");
        node.data = node.data.replace(/Jeong Hui-Won/gi, "Jung Heewon");
        node.data = node.data.replace(/Hui-Won/gi, "Heewon");
        node.data = node.data.replace(/Yu Joong-Hyeok/gi, "Yoo Jonghyuk");
        node.data = node.data.replace(/Joong-Hyeok/gi, "Jonghyuk");
        node.data = node.data.replace(/Yi Hyeon-Seong/gi, "Lee Hyunsung");
        node.data = node.data.replace(/Hyeon-Seong/gi, "Hyunsung");
        node.data = node.data.replace(/Yi Gil-Yeong/gi, "Lee Gilyoung");
        node.data = node.data.replace(/Gil-Yeong/gi, "Gilyoung");
        node.data = node.data.replace(/Shin Yu-Seung/gi, "Shin Yoosung");
        node.data = node.data.replace(/Yu-Seung/gi, "Yoosung");
        node.data = node.data.replace(/Jang Ha-Yeong/gi, "Jang Hayoung");
        node.data = node.data.replace(/Ha-Yeong/gi, "Hayoung");

        /* Side characters */
        //TBD
    }
    if (node.nodeType == 1 && node.nodeName != "SCRIPT") {
      for (var i = 0; i < node.childNodes.length; i++) {
        walkText(node.childNodes[i]);
      }
    }
  }
  walkText(document.body);
