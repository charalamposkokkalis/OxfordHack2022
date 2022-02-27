import Coin from "./Coin";
import { useState, useEffect } from "react";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:5000";

const Home = (props) => {
  // const [cryptos, setCryptos] = useState({ btc: 1, eth: 2 });
  const cryptos = {
    ada: 0.8975,
    bch: 309.3487,
    bsv: 84.9285,
    btc: 39323.7702,
    dash: 93.001,
    doge: 0.1276,
    etc: 28.139,
    eth: 2788.59,
    ltc: 109.6424,
    sol: 90.535,
    xmr: 154.3601,
    xrp: 0.7589,
    zec: 107.2972,
  };
  const [coins, setCoins] = useState([<Coin id={0} choices={cryptos} />]);
  const [solutions, setSolutions] = useState([]);
  const [comparisons, setComparisons] = useState([]);
  const [tons, setTons] = useState(0);

  const handleSubmit = (event) => {
    const reqString = { vals: [] };
    coins.map((coin) => {
      var crypto = document.getElementById(
        coin.props.id + " choose crypto"
      ).textContent;
      var quantity = parseFloat(
        document.getElementById(coin.props.id + " quantity").value
      );
      var usd = parseFloat(
        document.getElementById(coin.props.id + " value").textContent
      );

      reqString["vals"].push([crypto, quantity, usd]);
    });
    console.log(JSON.stringify(reqString));
    axios
      .post("http://localhost:5000/portfolio", JSON.stringify(reqString))
      .then((resp) => {
        setSolutions(resp.data.out[0]);
        setComparisons(resp.data.out[1]);
        setTons(resp.data.out[2]);
      });
  };

  const addButton = (e) => {
    setCoins([...coins, <Coin id={coins.length} choices={cryptos} />]);
  };

  const removeButton = (e) => {
    const list = [...coins];
    list.pop();
    setCoins(list);
  };

  return (
    <div>
      <form>
        <Grid container spacing={3}>
          <Grid item xs={4}>
            <Typography> Coins </Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography> Quantity </Typography>
          </Grid>
          <Grid item xs>
            <Typography> USD Value </Typography>
          </Grid>
        </Grid>
        {coins}
        <Button onClick={addButton}> Add </Button>
        <Button onClick={coins.length > 1 ? removeButton : null}>
          {" "}
          Remove{" "}
        </Button>
        <Button onClick={handleSubmit}>Save Choices </Button>
      </form>
      <Typography>
        {"Your crypto portfolio emits the equivalent of " +
          tons.toFixed(2) +
          " tons of carbon each year."}
      </Typography>
      <Typography>
        {coins.length > 0
          ? "Your carbon footprint is the equivalent of " +
            solutions.join(", or ")
          : ""}
      </Typography>
      <Typography>
        {coins.length > 0
          ? "To neutralize your carbon footprint, you could " +
            comparisons.join(", or ")
          : ""}
      </Typography>
    </div>
  );
};

export default Home;
