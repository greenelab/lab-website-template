// grid boundaries, left/top/right/bottom
const l = -1000;
const t = -1000;
const r = 800;
const b = 800;

// grid step size
const s = 100;

// grid svg path
let d = "";

// generate grid
for (let x = l; x <= r; x += s) d += `M ${x} ${t} L ${x} ${b}`;
for (let y = t; y <= b; y += s) d += `M ${l} ${y} L ${r} ${y}`;

// set path
document.querySelector(".grid").setAttribute("d", d);
