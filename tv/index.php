<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>Ibidem - Availabile Episodes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="/voidspace.css" rel="stylesheet" type="text/css" />
    <link href="/site.css" rel="stylesheet" type="text/css" />
    <link href="/jquery-ui-1.8.9.custom.css" rel="stylesheet" type="text/css" />
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js"></script>
</head>

<body>
    <h1>Ibidem</h1>
	<div id="header">
        <h2>Available Episodes</h2>
	</div>
        <div id="content">
            <ul>
            <?php
                define("NEW_DIR", "/volume1/video/series/0-NEW-0");
    
                $files = scandir(NEW_DIR);
                foreach ($files as $file) {
                    if (substr($file, -4) == ".srt" ||
                        $file == "." || $file == "..") {
	                        continue;
                    }
                    echo "<li><a href=\"next.php?next=" . urlencode($file) . "\" >" . $file . "</a></li>";
                }
            ?>

            </ul>
        </div>
        <div class="footer">
            <hr class="footer"/>
        </div>
    <?php
        include '../ga.inc';
    ?>
</body>
</html>
