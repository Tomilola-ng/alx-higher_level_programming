$(document).ready(function () {
  function fetchTranslation() {
    var languageCode = $("#language_code").val();
    var url = "https://www.fourtonfish.com/hellosalut/hello/" + languageCode;

    $.get(url, function (data) {
      $("#hello").text(data.hello);
    });
  }

  $("#btn_translate").click(fetchTranslation);
  $("#language_code").keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
