let $submitBtn = $("#submit-btn");
let checkWordUrl = "http://127.0.0.1:5000/word";
let $scoreBoard = $("#score-board");
let result = 0;

async function checkWord(word) {
  let response = await axios.post(checkWordUrl, {
    word,
  });
  let validityCheck = response.data.result;

  if (validityCheck === "ok") {
    addToScore(word);
  } else {
    alert("That word is not on the board.  Try again");
  }
}

$("form").on("submit", function (e) {
  e.preventDefault();
  let word = $("input").val();
  checkWord(word);
  $("#word-input").val("");
});

function addToScore(word) {
  //   console.log(`yay you got a point with ${word}`);
  let points = word.length;
  let updatedResult = result + points;
  result = updatedResult;
  $scoreBoard.text(result);
}
