<?php
    $actual_file_name = "../pdfs/spencerboucher-print.pdf";
    $saved_file_name = "spencerboucher.pdf"

    header("Content-Type: application/pdf");
    header("Content-Disposition: attachment; filename=$saved_file_name");
    header("Content-Length: " . filesize($actual_file_name));

    readfile($actual_file_name);
    exit;
?>
