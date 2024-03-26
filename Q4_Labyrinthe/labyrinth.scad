// base plate 
 translate([-0.5,-0.5,-1]){ 
 cube([41,41,1], center=false); 
 }  
// borders  
 translate([-0.5,-0.5,0]){ 
 cube([40,1,10], center=false); 
 } 
 translate([-0.5,-0.5,0]){ 
 cube([1,40,10], center=false); 
 } 
translate([-0.5,39.5,0]){ 
 cube([41,1,10], center=false); 
 } 
 translate([39.5,-0.5,0]){ 
 cube([1,41,10], center=false); 
 } 
 
 //interior walls 
 translate([5.0,30,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([15.0,10,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([15.0,20,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([25.0,10,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([25.0,20,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([25.0,30,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([35.0,10,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([35.0,30,5.0]){  
 cube([11,1,10], center=true); 
 } 
translate([30,25.0,5.0]){  
 rotate([0,0,90]){ 
 cube([11,1,10], center=true); 
 } 
 } 
