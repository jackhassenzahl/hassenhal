<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed"]);
    exit;
}

$text = $_POST["qrtext"] ?? "";
if ($text === "") {
    http_response_code(400);
    echo json_encode(["error" => "No input"]);
    exit;
}

// Create unique job ID
$job = uniqid("job_", true);

// Save job data
file_put_contents("jobs/queue/$job.txt", $text);

// Return job ID to client
echo json_encode(["job" => $job]);
