<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $text = $_POST["qrtext"] ?? "";
    if ($text === "") exit("No input.");

    // Remove old output if it exists
    if (file_exists("qr_card.stl")) unlink("qr_card.stl");

    // Run Python synchronously (PHP WILL WAIT)
    $cmd = "/var/www/html/hassenhal/card/.venv/bin/python /var/www/html/hassenhal/card/main.py " . escapeshellarg($text) . " 2>&1";
    echo shell_exec($cmd);
    $output = shell_exec($cmd);

    // Ensure file exists before sending
    if (!file_exists("qr_card.stl")) {
        exit("Generation failed:<pre>$output</pre>");
    }

    header("Content-Type: application/sla");
    header("Content-Disposition: attachment; filename=qr_card.stl");
    header("Content-Length: " . filesize("qr_card.stl"));
    readfile("qr_card.stl");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hassenhal</title>
    <link rel="icon" href="/images/logo.svg" type="image/svg">
    <link rel="stylesheet" type="text/css" href="/style/style.css">
    <link rel="stylesheet" type="text/css" media="(max-width: 700px)" href="/style/small.css">
    <link rel="stylesheet" type="text/css" media="(min-width: 701px) and (max-width: 900px)" href="/style/medium.css">
    <link rel="stylesheet" type="text/css" media="(min-width: 901px)" href="/style/large.css">
</head>
<body>
    <div id="navigation"></div>
    <main>
        <header>
            <h1>Under Construction<span id="sub-text"> (Always)</span></h1>
        </header>
        <form method="POST">
            <input type="text" name="qrtext" required>
            <button type="submit">Download STL</button>
        </form>
    </main>
    <footer>
        <p>© 2025 Jack Hassenzahl</p>
    </footer>
    <script src="/scripts/navbar.js"></script>
</body>
</html>