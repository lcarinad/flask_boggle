let $submitBtn = $("#submit-btn");
let checkWordUrl = "http://127.0.0.1:5000/word";
let endOfGameUrl = "http://127.0.0.1:5000/end";
let $scoreBoard = $("#score-board");
let $beginBtn = $("#begin-btn");
let $page = $("#game");

let result = 0;
$page.hide();

async function checkWord(word) {
  let response = await axios.post(checkWordUrl, {
    word,
  });
  let validityCheck = response.data.result;

  if (validityCheck === "ok") {
    addToScore(word);
  } else if (validityCheck === "not-on-board") {
    alert("That word is valid but it's not on the board.  Try again.");
  } else {
    alert("Not a word!");
  }
  console.log(response);
}

function addToScore(word) {
  //   console.log(`yay you got a point with ${word}`);
  let points = word.length;
  let updatedResult = result + points;
  result = updatedResult;
  $scoreBoard.text(result);
}
function createTimer() {
  let seconds = 59;
  let $counter = $("#counter");
  function tick() {
    seconds--;
    $counter.html("00:" + (seconds < 10 ? "0" : "") + seconds);
    if (seconds > 0) {
      setTimeout(tick, 1000);
    } else {
      alert("Times up!");
      $page.hide();
      $beginBtn.text("Play Again!").show();
      endOfGame(result);
    }
  }
  tick();
}

async function endOfGame(score) {
  await axios.post(endOfGameUrl, { score });
}

$("form").on("submit", function (e) {
  e.preventDefault();
  let word = $("input").val();
  checkWord(word);
  $("#word-input").val("");
});

$beginBtn.on("click", function (e) {
  e.preventDefault();
  $beginBtn.hide();
  result = 0;
  $scoreBoard.text(result);
  $page.show();
  createTimer();
});
