import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

const packageJsonPath = join(dirname(fileURLToPath(import.meta.url)), "..", "package.json");

describe("CLI aliases", () => {
	it("publishes spider-agent while retaining dek-agent compatibility", () => {
		const manifest = JSON.parse(readFileSync(packageJsonPath, "utf8")) as {
			bin?: Record<string, string>;
			piConfig?: { name?: string };
		};
		expect(manifest.bin?.["spider-agent"]).toBe(manifest.bin?.["dek-agent"]);
		expect(manifest.bin?.["spider-agent"]).toBeTruthy();
		expect(manifest.piConfig?.name).toBe("spider-agent");
	});
});
