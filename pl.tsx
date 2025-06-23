import type { Product } from "../../api/types/products";
import ProductCard from "./ProductCard";
import ky, { HTTPError } from "ky";

const getProducts = async (): Promise<Product[]> => {
  try {
    return await ky.get("").json<Product[]>();
  } catch (error) {
    if (error instanceof HTTPError) {
      console.error(error.response);
    }
    return [];
  }
};

const ProductList = async () => {
  const products = await getProducts();
  return (
    <div>
      Products:
      {products ? (
        products.map((product: Product) => {
          return <ProductCard data={product} />;
        })
      ) : (
        <div>Loading...</div>
      )}
    </div>
  );
};

export default ProductList;
