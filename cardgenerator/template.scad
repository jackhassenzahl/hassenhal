$fn = 60;

base_t = 0.4;
top_t = 0.4;
radius = 3.18;

width = 85.6;
depth = 53.98;

qr_size = depth;

qr_modules = 29;

module mirror_copy(v = [1, 0, 0]) {
    children();
    mirror(v) children();
}

module corner() {
    difference() {
        translate([0, 0, - round(radius + 1) / 2]) {
            cube(round(radius + 1));
        }
        
        translate([0, 0, - round(radius + 2) / 2]) {
            cylinder(round(radius + 2), r = radius);
        }
    }
}

module card_slice(t) {
    difference() {
        cube([width, depth, t], true);
        
        mirror_copy([0, 1, 0]) {
            mirror_copy() {
                translate([(width / 2) - radius, (depth / 2) - radius, 0]) {
                    corner();
                }
            }
        }
    }
}

union() {
    color("#00f") {
        difference() {
            translate([0, 0, top_t / 2]) {
                card_slice(top_t);
            }

            translate([- (qr_size / 2) - ((width / 2) - (qr_size / 2)), - qr_size / 2, 0]) {
                scale(qr_size / qr_modules) {
                    qr_code();
                }
            }
        }
    }

    color("#f00") {
        translate([0, 0, - base_t / 2]) {
            card_slice(base_t);
        }
    }
}
