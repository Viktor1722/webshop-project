import { useEffect, useState } from "react";
import Image from "next/image";
import Link from "next/link";

type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
  image: string;
};

export default function Products() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://localhost:8000/products/")
      .then((res) => res.json())
      .then((data) => {
        console.log("Fetched products:", data);
        if (Array.isArray(data)) {
          setProducts(data);
        } else {
          console.error("Unexpected API response format:", data);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        setLoading(false);
        setError(error.message);
      });
  }, []);

  if (loading) return <p className="text-center p-4 text-lg">Loading...</p>;
  if (error)
    return <p className="text-center p-4 text-red-500">Error: {error}</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6 text-center">Products</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.length > 0 ? (
          products.map((product) => (
            <Link
              href={`productInfo/${product.id}`}
              key={product.id}
              className="w-full"
            >
              <div className="bg-blue-50 rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                <div className="bg-blue-500 h-2 w-full">
                  <Image
                    src={product.image}
                    alt={product.name}
                    width={200}
                    height={300}
                  />
                </div>
                <div className="p-6">
                  <h2 className="text-xl font-semibold text-white mb-2">
                    {product.name}
                  </h2>
                  <p className="text-white mb-4">{product.description}</p>
                  <div className="flex justify-between items-center">
                    <p className="text-lg font-bold text-white">
                      ${product.price.toFixed(2)}
                    </p>
                    <button className="bg-blue-600 hover:bg-white text-white py-2 px-4 rounded-md transition-colors duration-300">
                      Add to Cart
                    </button>
                  </div>
                </div>
              </div>
            </Link>
          ))
        ) : (
          <p className="col-span-full text-center text-gray-500 p-8">
            No products available.
          </p>
        )}
      </div>
    </div>
  );
}
