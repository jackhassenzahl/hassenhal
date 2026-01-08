<?php
$queue = glob("jobs/queue/*.txt");

foreach ($queue as $jobfile) {
    $job = basename($jobfile, ".txt");
    $text = file_get_contents($jobfile);

    // Remove job from queue
    unlink($jobfile);

    // Run Python script for this job
    $cmd = "/var/www/html/hassenhal/card/.venv/bin/python /var/www/html/hassenhal/card/main.py "
         . escapeshellarg($text) . " "
         . escapeshellarg($job) . " 2>&1";

    $output = shell_exec($cmd);

    // If STL was not generated, log error
    if (!file_exists("jobs/done/$job.stl")) {
        file_put_contents("jobs/error/$job.log", $output);
    }
}
