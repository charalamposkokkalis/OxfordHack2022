import { Typography } from "@mui/material";

const Solutions = (props) => {
  const sols = [];
  props.sols.map((s) => sols.push(<Typography id={s}>{s}</Typography>));

  return <div>{sols}</div>;
};

export default Solutions;
