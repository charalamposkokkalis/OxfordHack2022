import { Typography } from "@mui/material";

const Solutions = (props) => {
  console.log(props.sols);
  return (
    <div>
      {" "}
      {props.sols.map((sol) => {
        <Typography sx={{ mt: 20 }}> {sol}</Typography>;
      })}{" "}
    </div>
  );
};

export default Solutions;
