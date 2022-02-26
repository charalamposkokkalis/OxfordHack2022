import Coin from "./Coin";
import { useState } from "react";
import Button from "@mui/material/Button";

const Home = (props) => {
  const cryptos = ["btc", "eth"];
  const [coins, setCoins] = useState([<Coin id={0} choices={cryptos} />]);

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
