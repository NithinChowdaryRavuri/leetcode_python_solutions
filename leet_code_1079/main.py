class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(tile_count: Counter) -> int:
            combinations = 0

            for tile, count in tile_count.items():
                if count > 0:
                    combinations += 1
                    tile_count[tile] -= 1
                    combinations += dfs(tile_count)
                    tile_count[tile] += 1

            return combinations
            
        tile_count = Counter(tiles)
        return dfs(tile_count)