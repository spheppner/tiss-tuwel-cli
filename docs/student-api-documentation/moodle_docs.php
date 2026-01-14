<?php

/**
 * Prints the external functions in markdown format for the documentation in mkdocs
 */

require_once('../../config.php');
require_once($CFG->libdir . '/adminlib.php');
require($CFG->dirroot . '/webservice/lib.php');

admin_externalpage_setup('webservicedocumentation');

// get all the function descriptions
$functions = $DB->get_records('external_functions', array('services' => 'moodle_mobile_app'), 'name');
$functiondescs = array();
foreach ($functions as $function) {
    $functiondescs[$function->name] = external_api::external_function_info($function);
}

$documentationhtml = "";
$br = html_writer::empty_tag('br', array());

function printParams($params, $indent = "") {
    foreach ($params as $key => $value) {
        echo $indent . $key . " ";


        if (!empty($value->content)) {
            if ($value->required == 2) {
                echo "**Optional** ";
            }
            echo "// $value->desc" . "\n";

            echo $indent . "[" . "\n";
            echo $indent . "\t{" . "\n";
            if (!empty($value->content->keys)) {
                printParams($value->content->keys, $indent . "\t\t");
            }else {
                echo "\t\t";
                printParam($value->content);
            }

            echo $indent . "\t}" . "\n";
            echo $indent . "]" . "\n";

        } else if (!empty($value->keys)) {
            if ($value->required == 2) {
                echo "**Optional** ";
            }
            echo "// $value->desc" . "\n";

            echo $indent . "{" . "\n";
            printParams($value->keys, $indent . "\t");
            echo $indent . "}" . "\n";

        } else {
            printParam($value);
        }

    }
}


function printParam($value) {
    switch ($value->type) {
        case PARAM_BOOL: // 0 or 1 only for now
        case PARAM_INT:
            $type = 'int';
            break;
        case PARAM_FLOAT;
            $type = 'double';
            break;
        default:
            $type = 'string';
    }
    echo "$type ";
    if ($value->required == 2) {
        echo "**Optional** ";
    }
    echo "// $value->desc" . "\n";
}

foreach ($functions as $functionname => $description) {

    echo "<details>";
    echo "\n";

    echo "<summary>$description->name</summary>";
    echo "\n";
    echo "<br/>";
    echo "\n";

    echo "<p>$description->description</p>";
    echo "\n";

    echo "<h3>Parameters</h3>";
    echo "\n";

    if (!empty($description->parameters_desc->keys)) {
        echo "```" . "\n";
        printParams($description->parameters_desc->keys);
        echo "```" . "\n";
    }else {
        echo "<strong>No Parameters.</strong><br/>";
        echo "\n";
    }

    echo "\n";
    echo "<h3>Returns</h3>";
    echo "\n";

    if (!empty($description->returns_desc->keys)) {
        echo "```" . "\n";
        printParams($description->returns_desc->keys);
        echo "```" . "\n";
    }else {
        echo "<strong>No Return.</strong><br/>";
        echo "\n";
    }

    echo "\n";

    echo "<hr/>";
    echo "\n";

    echo "</details>";
    echo "\n";
}

