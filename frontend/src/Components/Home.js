import Coin from "./Coin";
import { useState } from "react";
import Button from "@mui/material/Button";
// import axios from "axios";

const Home = (props) => {
  // const [cryptos, setCryptos] = useState({ btc: 1, eth: 2 });
  const cryptos = {
    ada: 0.8975,
    bch: 309.3487,
    bsv: 84.9285,
    btc: 39323.7702,
    btg: 29.1493,
    dash: 93.001,
    doge: 0.1276,
    etc: 28.139,
    eth: 2788.59,
    ltc: 109.6424,
    sol: 90.535,
    vtc: 0.2679,
    xmr: 154.3601,
    xrp: 0.7589,
    zec: 107.2972,
  };
  // const [loading, setLoading] = useState(false);
  const [coins, setCoins] = useState([<Coin id={0} choices={cryptos} />]);

  /*
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const res = await axios.get("http://localhost:5000/coins");
      setCryptos(res.data);
      setLoading(false);
    };
    fetchData();
  }, []);
  */

  const handleSubmit = (event) => {
    coins.map((coin) => {
      var crypto = document.getElementById(
        coin.props.id + " choose crypto"
      ).textContent;
      var quantity = document.getElementById(coin.props.id + " quantity").value;

      console.log(`Crypto: ${crypto} Quantity: ${quantity}`);
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
        {coins}
        <Button onClick={addButton}> Add </Button>
        <Button onClick={removeButton}> Remove Last </Button>
        <Button onClick={handleSubmit}>Save Choices </Button>
      </form>
    </div>
  );
};

export default Home;
