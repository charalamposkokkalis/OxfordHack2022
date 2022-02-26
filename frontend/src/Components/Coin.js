import { useState } from "react";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";

const Coin = (props) => {
  const [crypto, setCrypto] = useState("");

  const handleChange = (event) => {
    setCrypto(event.target.value);
  };

  return (
    <Box
      component="form"
      sx={{
        "& .MuiTextField-root": { m: 1, width: "25ch" },
      }}
      noValidate
      autoComplete="off"
    >
      <FormControl>
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <InputLabel id="demo-simple-select-label">Coin</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={crypto}
              label="Coin"
              onChange={handleChange}
            >
              {props.choices.map((choice) => (
                <MenuItem value={choice}>{choice}</MenuItem>
              ))}
            </Select>
          </Grid>
          <Grid item xs={4}>
            <TextField required />
          </Grid>
          <Grid item xs={4}>
            <Button variant="contained"> Add new </Button>
          </Grid>
        </Grid>
      </FormControl>
    </Box>
  );
};

export default Coin;
