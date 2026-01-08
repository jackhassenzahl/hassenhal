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
<body>
<form method="POST">
    <input type="text" name="qrtext" required>
    <button type="submit">Download STL</button>
</form>
</body>
</html>
