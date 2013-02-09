<?php
    define("SERIES_ROOT", "/volume1/video/series");
    define("NEXT_PATTERN", "next$[0-9]+x[0-9]+.py");

    function scan_for_file($root, $target) {
        $files = scandir($root);
        if (in_array($target, $files)) {
            return $root;
        }
        $dirs = array_filter($files, "is_dir");
        foreach ($dirs as $dir) {
            $result = scan_for_file($dir, $target);
            if (!is_null($result)) {
                return $result;
            }
        }
        return NULL;
    }

    function find_next_file($dir) {
        $files = scandir($dir);
        $matches = preg_grep(NEXT_PATTERN, $files);
        if (count($matches) > 0) {
            return $matches[0];
        }
        return NULL;
    }

    $file = urldecode($_GET["next"]);
    $season_dir = scan_for_file(SERIES_ROOT, $file);
    $series_dir = dirname($season_dir);
    $next_file = find_next_file($series_dir);
    system("python " . $next_file);

    header("index.php", 301);