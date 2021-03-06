#include "DD4hep/DetFactoryHelper.h"
#include "DetectorDescription/Core/interface/DDSplit.h"
#include "DetectorDescription/DDCMS/interface/DDPlugins.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

//#define EDM_ML_DEBUG

static long algorithm(dd4hep::Detector& /* description */,
                      cms::DDParsingContext& ctxt,
                      xml_h e,
                      dd4hep::SensitiveDetector& /* sens */) {
  cms::DDNamespace ns(ctxt, e, true);
  cms::DDAlgoArguments args(ctxt, e);
  // Header section
  std::string parentName = DDSplit(args.parentName()).first;
  std::string cellMat = args.value<std::string>("CellMaterial");                        //Cell material
  double cellDx = args.value<double>("CellDx");                                         //Cell size (x)
  double cellDy = args.value<double>("CellDy");                                         //Cell size (y)
  double cellDz = args.value<double>("CellDz");                                         //Cell size (z)
  double startY = args.value<double>("StartY");                                         //Starting Y for Cell
  std::vector<std::string> childName = args.value<std::vector<std::string> >("Child");  //Children name
  std::vector<int> number = args.value<std::vector<int> >("Number");                    //Number of cells
  std::vector<int> size = args.value<std::vector<int> >("Size");                        //Number of children
  std::vector<int> type = args.value<std::vector<int> >("Type");                        //First child
#ifdef EDM_ML_DEBUG
  edm::LogVerbatim("HCalGeom") << "DDHCalForwardAlgo: Cell material " << cellMat << "\tCell Size " << cellDx << ", "
                               << cellDy << ", " << cellDz << "\tStarting Y " << startY << "\tChildren " << childName[0]
                               << ", " << childName[1] << "\n               "
                               << "          Cell positioning done for " << number.size() << " times";
  for (unsigned int i = 0; i < number.size(); ++i)
    edm::LogVerbatim("HCalGeom") << "\t" << i << " Number of children " << size[i] << " occurence " << number[i]
                                 << " first child index " << type[i];
  edm::LogVerbatim("HCalGeom") << "DDHCalForwardAlgo debug: Parent " << args.parentName() << " NameSpace " << ns.name();
#endif

  dd4hep::Volume parent = ns.volume(args.parentName());
  dd4hep::Material matter = ns.material(cellMat);

  double ypos = startY;
  int box = 0;
  for (unsigned int i = 0; i < number.size(); i++) {
    double dx = cellDx * size[i];
    int indx = type[i];
    for (int j = 0; j < number[i]; j++) {
      box++;
      std::string name = parentName + std::to_string(box);
      dd4hep::Solid solid = dd4hep::Box(dx, cellDy, cellDz);
      ns.addSolidNS(ns.prepend(name), solid);
#ifdef EDM_ML_DEBUG
      edm::LogVerbatim("HCalGeom") << "DDHCalForwardAlgo: " << solid.name() << " Box made of " << cellMat << " of Size "
                                   << dx << ", " << cellDy << ", " << cellDz;
#endif
      dd4hep::Volume glog(solid.name(), solid, matter);
      ns.addVolumeNS(glog);

      dd4hep::Position r0(0.0, ypos, 0.0);
      dd4hep::Rotation3D rot;
      parent.placeVolume(glog, box, dd4hep::Transform3D(rot, r0));
#ifdef EDM_ML_DEBUG
      edm::LogVerbatim("HCalGeom") << "DDHCalForwardAlgo: " << solid.name() << " number " << box << " positioned in "
                                   << parent.name() << " at " << r0 << " with " << rot;
#endif

      double xpos = -dx + cellDx;
      ypos += 2 * cellDy;
      indx = 1 - indx;

      for (int k = 0; k < size[i]; ++k) {
        dd4hep::Position r1(xpos, 0.0, 0.0);
        glog.placeVolume(ns.volume(childName[indx]), k + 1, dd4hep::Transform3D(rot, r1));
#ifdef EDM_ML_DEBUG
        edm::LogVerbatim("HCalGeom") << "DDHCalForwardAlgo: " << childName[indx] << " number " << k + 1
                                     << " positioned in " << glog.name() << " at " << r1 << " with " << rot;
#endif
        xpos += 2 * cellDx;
      }
    }
  }
#ifdef EDM_ML_DEBUG
  edm::LogVerbatim("HCalGeom") << "<<== End of DDHCalForwardAlgo construction";
#endif
  return 1;
}

// first argument is the type from the xml file
DECLARE_DDCMS_DETELEMENT(DDCMS_hcal_DDHCalForwardAlgo, algorithm);
