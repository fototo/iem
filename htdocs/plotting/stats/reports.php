<?php
include("../../../config/settings.inc.php");
include("$rootpath/include/database.inc.php");
$connection = iemdb("access");

$network = isset($_GET["network"]) ? $_GET["network"] : "IA_ASOS";

$query1 = "SET TIME ZONE 'GMT'";
$query2 = "select count(*), tvalid from ( 
    select station, to_char(valid, 'mmdd/HH24') as tvalid, count(*)
    from current_log WHERE network= '$network' GROUP by station, tvalid) as foo
  GROUP by tvalid ORDER by tvalid ASC";

$result = pg_exec($connection, $query1);
$result = pg_exec($connection, $query2);

$ydata = array();
$xlabel= array();


$j = 0;
for( $i=0; $row = @pg_fetch_array($result,$i); $i++) 
{
  $ydata[$i]  = $row["count"];
  $xlabel[$i] = $row["tvalid"];
}

pg_close($connection);


include ("$rootpath/include/jpgraph/jpgraph.php");
include ("$rootpath/include/jpgraph/jpgraph_line.php");

$goal = Array("awos" => 35, "asos" => 15, "rwis" => 50);

// Create the graph. These two calls are always required
$graph = new Graph(600,400,"example3");
$graph->SetScale("textlin",0,50);
$graph->img->SetMargin(40,20,50,100);

//$graph->xaxis->SetFont(FS_FONT1,FS_BOLD);
$graph->xaxis->SetTickLabels($xlabel);
$graph->xaxis->SetLabelAngle(90);

$graph->yaxis->scale->ticks->Set(5,1);

$graph->title->Set("Total $network observations per valid time");
//$graph->subtitle->Set("Total Possible: ". $goal[$network] );
$graph->title->SetFont(FF_FONT1,FS_BOLD,16);
$graph->yaxis->SetTitle("Total Valid Obs");
$graph->yaxis->title->SetFont(FF_FONT1,FS_BOLD,12);
$graph->xaxis->SetTitle("Valid GMT Time");
$graph->xaxis->SetTitleMargin(55);
$graph->xaxis->title->SetFont(FF_FONT1,FS_BOLD,12);



// Create the linear plot
$lineplot=new LinePlot($ydata);
$lineplot->SetColor("red");

// Add the plot to the graph
$graph->Add($lineplot);

// Display the graph
$graph->Stroke();
?>

