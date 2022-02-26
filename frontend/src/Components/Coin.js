import { useState } from "react";
import MenuItem from "@mui/material/MenuItem";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";

const Coin = (props) => {
  const [crypto, setCrypto] = useState("");
  const [quantity, setQuantity] = useState(0);

  const handleChange = (event) => {
    setCrypto(event.target.value);
    setQuantity(0);
  };

  return (
    <div>
      <Grid container spacing={3}>
        <Grid item xs={4}>
          <TextField
            id={props.id + " choose crypto"}
            select
            label="Coin"
            value={crypto}
            onChange={handleChange}
            helperText="Please select your crypto"
          >
            {Object.keys(props.choices).map((choice) => (
              <MenuItem value={choice}>{choice}</MenuItem>
            ))}
          </TextField>
        </Grid>
        <Grid item xs={4}>
          <TextField
            id={props.id + " quantity"}
            value={quantity}
            required
            onChange={(e) => setQuantity(e.target.value)}
          />
        </Grid>
        <Grid item xs>
          <Typography id={props.id + " value"}>
            {" "}
            {quantity
              ? parseFloat(quantity) *
                props.choices[
                  document.getElementById(props.id + " choose crypto")
                    .textContent
                ]
              : 0}{" "}
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default Coin;
