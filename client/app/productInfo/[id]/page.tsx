// pages/productInfo/[id].tsx
"use client"; // Ensures this page runs on the client-side only
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Image from "next/image";

type Product = {
  id: number;
  name: string;
  description: string;
  price: number;
  image: string;
};

export default function ProductInfo() {
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const params = useParams();

  const id = params?.id;

  // Wait until the component is mounted and the router has the necessary information
  useEffect(() => {
    if (!id) return; // Ensure we have an id

    // Fetch product details based on the id
    fetch(`http://localhost:8000/products/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setProduct(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, [id]); // Dependency on 'id' ensures this only runs when the id changes

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!product) return <p>Product not found.</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">{product.name}</h1>
      <div className="flex flex-col md:flex-row gap-6">
        <div className="w-full md:w-1/2">
          <Image
            src={product.image}
            alt={product.name}
            width={300}
            height={450}
          />
        </div>
        <div className="w-full md:w-1/2">
          <p className="mb-4">{product.description}</p>
          <p className="text-lg font-bold mb-4">${product.price.toFixed(2)}</p>
          <button className="bg-blue-600 text-white py-2 px-4 rounded-md">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}
