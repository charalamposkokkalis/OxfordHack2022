import Coin from "./Coin";
import { useState } from "react";
import Button from "@mui/material/Button";

const Home = (props) => {
  const cryptos = ["btc", "eth"];
  const [numCoins, setNumCoins] = useState(1);
  const [coins, setCoins] = useState([<Coin choices={cryptos} />]);

  return (
    <div>
      <form>{coins}</form>
      <Button onClick={() => setCoins([...coins, <Coin choices={cryptos} />])}>
        {" "}
        Add{" "}
      </Button>
    </div>
  );
};

export default Home;
