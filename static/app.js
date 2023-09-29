let $submitBtn = $("#submit-btn");
let checkWordUrl = "http://127.0.0.1:5000/word";

async function checkWord(word) {
  let response = await axios.post(checkWordUrl, {
    word,
  });
  return response.data;
}

$("form").on("submit", function (e) {
  e.preventDefault();
  let word = $("input").val();
  checkWord(word);
  $("#word-input").val("");
});
