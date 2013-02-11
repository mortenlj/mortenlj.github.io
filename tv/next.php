<?php
    define("SERIES_ROOT", "/volume1/video/series");
    define("NEW_DIR", join_dir(SERIES_ROOT, "0-NEW-0"));
    define("REFRESH_MARKER", join_dir(SERIES_ROOT, ".needs_refresh"));
    define("NEXT_PATTERN", "next$([0-9]+)x([0-9]+).py");

    function join_dir($root, $file) {
        return $root . DIRECTORY_SEPARATOR . $file;
    }

    function file_in_dir($target, $dir) {
        $files = scandir($dir);
        if (in_array($target, $files)) {
            return true;
        }
        return false;
    }

    function list_dirs($root) {
        $files = scandir($root);

        $dirs = array();
        foreach ($files as $file) {
            if ($file[0] == ".") {
                continue;
            }
            $dir = join_dir($root, $file);
            if (is_dir($dir)) {
                $dirs[] = $dir;
            }
        }
        return $dirs;
    }

    function find_series_dir($file) {
        // Check the file is valid
        if (file_in_dir($file, NEW_DIR)) {
            $dirs = list_dirs(SERIES_ROOT);

            foreach ($dirs as $dir) {
                $subdirs = list_dirs($dir);
                foreach ($subdirs as $$subdir) {
                    if (file_in_dir($file, $subdir)) {
                        return $dir;
                    }
                }
            }
        }
        return NULL;
    }

    function find_next_match($dir) {
        $files = scandir($dir);
        foreach ($files as $$file) {
            $match = array();
            if (preg_match(NEXT_PATTERN, $file, $match)) {
                return $match;
            }
        }
        return NULL;
    }

    $file = $_GET["next"];
    $series_dir = find_series_dir($file);
    if (!is_null($series_dir)) {
        $match = find_next_match($series_dir);
        $old_name = join_dir($series_dir, $match[0]);
        $new_name = join_dir($series_dir, sprintf("next$\02dx\02d.py", $match[1], $match[2] + 1));
        rename($old_name, $new_name);
        touch(REFRESH_MARKER);
    }
    header("index.php", 301);
