let rotateX;
let rotateZ;

const resetView = () => {
  rotateX = 70;
  rotateZ = 0;

  updateView();
};

const rotateView = ({ clientX, clientY }) => {
  const { left, top, width, height } = document.body.getBoundingClientRect();

  rotateX = 80 - 20 * ((clientY - top) / height);
  rotateZ = 10 - 20 * ((clientX - left) / width);

  updateView();
};

const updateView = () => {
  document.body.style.setProperty("--rotateX", rotateX + "deg");
  document.body.style.setProperty("--rotateZ", rotateZ + "deg");
};

resetView();

const replayAnimations = () => {
  document.getAnimations().forEach((anim) => {
    anim.finish();
    anim.play();
  });
};

document.documentElement.addEventListener("mouseleave", resetView);
document.documentElement.addEventListener("mousemove", rotateView);
document.documentElement.addEventListener("click", replayAnimations);
