<?php
header('Content-Type: application/json');

$job = $_GET["job"] ?? "";
if (!$job) {
    echo json_encode(["status" => "unknown"]);
    exit;
}

if (file_exists("jobs/done/$job.stl")) {
    echo json_encode(["status" => "done"]);
    exit;
}

if (file_exists("jobs/error/$job.log")) {
    echo json_encode(["status" => "error"]);
    exit;
}

echo json_encode(["status" => "working"]);
