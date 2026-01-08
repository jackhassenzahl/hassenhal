<?php
$job = $_GET["job"] ?? "";
$file = "jobs/done/$job.stl";

if (!file_exists($file)) {
    http_response_code(404);
    exit("File not ready or does not exist");
}

header("Content-Type: application/sla");
header("Content-Disposition: attachment; filename=qr_card.stl");
header("Content-Length: " . filesize($file));
readfile($file);
