from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Map
from collections import deque
from .serializers import MapSerializer

class MapView(APIView):
    def get(self, request, map_id=None):
        if map_id:
            map_obj = get_object_or_404(Map, id=map_id)
            serializer = MapSerializer(map_obj)
            return Response(serializer.data)
        else:
            maps = Map.objects.all()
            serializer = MapSerializer(maps, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MapNavigationView(APIView):
    def get(self, request, map_id):
        try:
            start_row = int(request.query_params.get('start_row'))
            start_col = int(request.query_params.get('start_col'))
            end_row = int(request.query_params.get('end_row'))
            end_col = int(request.query_params.get('end_col'))
            
            map_obj = get_object_or_404(Map, id=map_id)
            
            if not (map_obj.is_valid_position(start_row, start_col) and 
                   map_obj.is_valid_position(end_row, end_col)):
                return Response(
                    {'error': 'Invalid coordinates'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            path_exists = self.bfs_path_check(
                map_obj.layout,
                (start_row, start_col),
                (end_row, end_col)
            )
            
            return Response({'path_exists': path_exists})
            
        except (TypeError, ValueError) as e:
            return Response(
                {'error': f'Invalid parameters: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def bfs_path_check(self, grid, start, end):
        rows, cols = len(grid), len(grid[0])
        queue = deque([start])
        visited = set([start])

        print(f"\n Start: {start}, End: {end} \n")

        while queue:
            r, c = queue.popleft()
            print(f"Visiting: ({r}, {c})")
            print(f"Updated Queue: ({list(queue)}) \n")

            if (r, c) == end:
                print("Path found \n")
                return True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 'R' and (nr, nc) not in visited:
                        print("Valid move \n")
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                    else:
                        print("Blocked or visited \n")
                else:
                    print("Out of bounds \n")

        print("No path found \n")
        return False