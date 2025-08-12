import type { Product } from "../../api/types/products";

interface ListCardProps {
  data: Product;
  // subscribe to product button, etc
}

const ProductCard: React.FC<ListCardProps> = (props) => {
  const { data } = props;

  return (
    <div>
      Name: {data.name}, URL: {data.url}
    </div>
  );
};

export default ProductCard;
