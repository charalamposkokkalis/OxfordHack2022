import Coin from "./Coin";

const Home = (props) => {
  const cryptos = ["btc", "eth"];
  return <Coin choices={cryptos} />;
};

export default Home;
