<?php 
/*
 * Attempt to actually document the RASTERs the IEM produces and stores
 * within its archives
 */
include("../../config/settings.inc.php");
define("IEM_APPID", 82);
require_once "../../include/database.inc.php";
include_once "../../include/myview.php";
$t = new MyView();
$mesosite = iemdb("mesosite");

$t->title = "GIS RASTER Documentation";

$rid = isset($_GET["rid"]) ? intval($_GET["rid"]) : 1;


$table = "";
$rs = pg_query($mesosite, "SELECT * from iemrasters
  ORDER by name ASC");

$rname = "";
$runits = "";
for($i=0;$row=@pg_fetch_assoc($rs,$i);$i++){
	if ($rid == intval($row["id"])){
		$rname = $row["name"];
		$runits = $row["units"];
		$t->title = sprintf("RASTER info for %s", $rname);
	}
	$table .= sprintf("<tr><td><a href=\"?rid=%s\">%s</a></td>"
			."<td>%s</td><td>%s</td></tr>\n", $row["id"], $row["name"],
			$row["description"], $row["units"]);

}

function rgb2html($r, $g, $b)
{
	if (is_array($r) && sizeof($r) == 3)
		list($r, $g, $b) = $r;

	$r = intval($r); $g = intval($g);
	$b = intval($b);

	$r = dechex($r<0?0:($r>255?255:$r));
	$g = dechex($g<0?0:($g>255?255:$g));
	$b = dechex($b<0?0:($b>255?255:$b));

	$color = (strlen($r) < 2?'0':'').$r;
	$color .= (strlen($g) < 2?'0':'').$g;
	$color .= (strlen($b) < 2?'0':'').$b;
	return '#'.$color;
}

$table2 = "";
if ($rid > 0){
	$rs = pg_prepare($mesosite, "-SELECT", "SELECT * from iemrasters_lookup"
			." WHERE iemraster_id = $1 ORDER by coloridx ASC");
	$rs = pg_execute($mesosite, "-SELECT", Array($rid));
	for($i=0;$row=@pg_fetch_assoc($rs,$i);$i++){
		$table2 .= sprintf("<tr><td>%s</td><td>%s</td><td>%s</td>"
				."<td>%s</td><td>%s</td><td>%s</td></tr>\n", $row["coloridx"], 
				$row["value"],
				$row["r"], $row["g"], $row["b"], 
				rgb2html($row["r"], $row["g"], $row["b"]));
	
	}
}

$t->content = <<<EOF
<ol class="breadcrumb">
 <li><a href="/GIS/">GIS Mainpage</a></li>
 <li class="active">IEM RASTER Lookup Tables</li>
</ol>

<h3>IEM RASTER Lookup Tables</h3>

<p>The IEM produces a number of RASTER images meant for GIS use. These RASTERs
are typically provided on the IEM website as 8 bit PNG images.  This means there
are 256 slots available for a binned value to be placed.  This page attempts to
document these RASTER images and provide the lookup table of PNG index to an 
actual value. Click on the item in the "Label" column to get the lookup 
table below.</p>

<p><table class="table table-condensed table-striped">
<thead><tr><th>Label</th><th>Description</th><th>Units</th></tr></thead>
<tbody>
{$table}
</tbody>
</table>

<h3>Lookup Table for {$rname}</h3>

<div class="alert alert-info">Would it help you to have the information below
in a different format?  Please <a class="alert-link" 
href="/info/contacts.php"><i class="glyphicon glyphicon-earphone"></i> contact us</a> 
if so!</div>

<table class="table table-condensed table-striped">
<thead><tr><th>Color Index</th><th>Value ({$runits})</th><th>Red</th><th>Green</th>
<th>Blue</th><th>HEX</th></tr></thead>
<tbody>
{$table2}
</tbody>
</table>

EOF;
$t->render('single.phtml');
?>
