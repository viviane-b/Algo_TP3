translate([10,5,-1]){
cube([8,20,30]);
    }
    
translate([-0.5,-0.5,-1]){
cube([131,131,1], center=false);
}
translate([60.0,65.0,5.0]){
//rotate([0,0,90]){
cube([11,1,10], center=true);
}
//}

// borders
translate([-0.5,-0.5,0]){
cube([121,1,10], center=false);
}
translate([-0.5,-0.5,0]){
cube([1,131,10], center=false);
}
translate([-0.5,129.5,0]){
cube([131,1,10], center=false);
}
translate([129.5,-0.5,0]){
cube([1,131,10], center=false);
}

