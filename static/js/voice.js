function record() {
  var recognition = new webkitSpeechRecognition();

  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = "en-GB";

  recognition.onresult = function (event) {
    //console.log(event);
    document.getElementById("speechToText").value =
      event.results[0][0].transcript;
  };

  recognition.start();
}