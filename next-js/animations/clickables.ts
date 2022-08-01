export const rClickables = {
  initial: {
    scale: 0.6,
    opacity: 0,
    x: 30,
  },
  animate: {
    scale: 1,
    opacity: 1,
    x: 0,
    transition: {
      type: "spring",
      stiffness: 500,
      when: "beforeChildren",
      staggerChildren: 0.3,
    },
  },
  hover: {
    scale: 1.1,
    transition: {
      type: "spring",
      stiffness: 500,
    },
  },
  tap: {
    scale: 0.9,
  },
};

export const lClickables = {
  initial: {
    scale: 0.6,
    opacity: 0,
    x: -30,
  },
  animate: {
    scale: 1,
    opacity: 1,
    x: 0,
    transition: {
      type: "spring",
      stiffness: 500,
      when: "beforeChildren",
      staggerChildren: 0.3,
    },
  },
  hover: {
    scale: 1.1,
    transition: {
      type: "spring",
      stiffness: 500,
    },
  },
  tap: {
    scale: 0.9,
  },
};
