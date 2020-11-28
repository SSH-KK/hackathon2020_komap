import React from "react";
import Link from "next/link";

import ExampleComponent from "components/ExampleComponent";
import PowerfulComponent from "components/PowerfulComponent";

export default function Home() {
  return (
    <>
      <ExampleComponent />
      <PowerfulComponent />
      <Link href="/counter">
        <a>Simplifyed counter</a>
      </Link>
    </>
  );
}
