<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Move Object with Cursor</title>
<style>
  body, html {
    height: 100%;
    margin: 0;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  #container {
    width: 100vw;
    height: 100vh;
    position: relative;
    background-color: lightgrey;
  }
  #movable-object {
    width: 50px;
    height: 50px;
    position: absolute;
    background-color: red;
    border-radius: 50%;
  }
</style>
</head>
<body>

<div id="container">
  <div id="movable-object"></div>
</div>

<script src="script.js"></script>
</body>
</html>
