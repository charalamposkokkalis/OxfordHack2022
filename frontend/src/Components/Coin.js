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
      <Grid container spacing={3} sx={{ width: 700 }}>
        <Grid item xs={4}>
          <TextField
            id={props.id + " choose crypto"}
            select
            label="Coin"
            value={crypto}
            onChange={handleChange}
            sx={{ width: 90, mt: 2 }}
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
            label={crypto}
            onChange={(e) => setQuantity(e.target.value)}
            sx={{ mt: 2, width: 160 }}
          />
        </Grid>
        <Grid item xs>
          <Typography id={props.id + " value"} sx={{ mt: 2 }}>
            {" "}
            {quantity
              ? parseFloat(quantity) *
                props.choices[
                  document.getElementById(props.id + " choose crypto")
                    .textContent
                ].toFixed(2)
              : 0}{" "}
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default Coin;
